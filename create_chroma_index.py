import os
import json
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import chromadb

# Load environment variables from .env
load_dotenv()

# Initialize ChromaDB client - try Cloud first, then local
client = None

try:
    # Try ChromaDB Cloud if credentials are available
    if "CHROMA_TENANT" in os.environ and "CHROMA_API_KEY" in os.environ:
        print("Connecting to ChromaDB Cloud...")
        client = chromadb.CloudClient(
            tenant=os.environ["CHROMA_TENANT"],
            database=os.environ.get("CHROMA_DATABASE", "default_database"),
            api_key=os.environ["CHROMA_API_KEY"]
        )
        print("✅ Connected to ChromaDB Cloud")
    else:
        print("ChromaDB Cloud credentials not found, using local client...")
        # Use local persistent client
        client = chromadb.PersistentClient(path="./chroma_db")
        print("✅ Connected to local ChromaDB")
        
except Exception as e:
    print(f"Failed to connect to ChromaDB Cloud: {e}")
    print("Falling back to local ChromaDB...")
    client = chromadb.PersistentClient(path="./chroma_db")
    print("✅ Connected to local ChromaDB")

# Create or get collection
collection = client.get_or_create_collection("gita_verses")

# Load data
with open("gita_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
metadatas = []
ids = []

def safe_meta_value(val):
    if val is None:
        return ""
    if isinstance(val, (int, float, str, bool)):
        return val
    return str(val)

# Prepare documents
for i, item in enumerate(data):
    text = item.get("chapter_text") or item.get("text") or ""
    documents.append(text)
    metadatas.append({
        "chapter_number": safe_meta_value(item.get("chapter_number")),
        "verse_number": safe_meta_value(item.get("verse_number")),
        "source": "gita"
    })
    ids.append(f"verse_{i}")

# Upload in batches
batch_size = 100
for i in range(0, len(documents), batch_size):
    collection.add(
        documents=documents[i:i+batch_size],
        metadatas=metadatas[i:i+batch_size],
        ids=ids[i:i+batch_size]
    )

print(f"✅ Uploaded {len(documents)} verses to ChromaDB Cloud!")
