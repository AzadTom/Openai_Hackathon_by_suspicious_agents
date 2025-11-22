import os
import json
import asyncio
from Custom_Chroma_Rag import addDocuments
from pathlib import Path

project_root = Path(__file__).parent
json_tracks = f"{project_root}/csv_file_track.json"


async def load_added_files():
    if not os.path.exists(json_tracks):
        with open(json_tracks, "w") as f:
            json.dump([], f)
        return []
    with open(json_tracks, "r") as f:
        return json.load(f)


async def save_added_files(files_path):
    with open(json_tracks, "w") as f:
        json.dump(files_path, f, indent=2)


async def main():
    added_files = await load_added_files()
    for file in os.listdir(project_root):
        if file.endswith(".csv"):
            csv_file_path = project_root / file
            if file in added_files:
                print(f"Skipping {file} → already added")
                continue
            collection_name = file.replace(".csv", "")
            print(f"Adding {file} to Chroma as collection '{collection_name}'...")
            await addDocuments.create(str(csv_file_path), collection_name)
            added_files.append(file)
            await save_added_files(added_files)


if __name__ == "__main__":
    asyncio.run(main())
