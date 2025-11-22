from Custom_Chroma_Rag import AsyncChromaDB


async def deleteCollection(collection_name: str = "Default"):
    if collection_name=='Default':
        raise RuntimeError("Default collection can't be initialized, please pass collection_name")
    deleteClient = AsyncChromaDB(collection_name=collection_name)
    await deleteClient.client_init_async()
    client = deleteClient.client
    await client.delete_collection(name=collection_name)
    print(f"✅ Collection --> {collection_name} is deleted successfully\n")


if __name__ == "__main__":
    import asyncio
    response=input("Type your collection name for deletion: ")
    asyncio.run(deleteCollection(response))
