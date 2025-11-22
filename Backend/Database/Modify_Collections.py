from Custom_Chroma_Rag import AsyncChromaDB


async def modifyCollection(collection_name: str = "Default"):
    if collection_name=='Default':
        raise RuntimeError("Default collection can't be initialized, please pass collection_name")
    modifyClient = AsyncChromaDB(collection_name=collection_name)
    await modifyClient.client_init_async()
    await modifyClient.collection.modify(
        name=collection_name, metadata={"description": "new description"}
    )
    print(f"✅ Collection --> {collection_name} is modified successfully\n")


if __name__ == "__main__":
    import asyncio
    response=input("Type your collection name to modify: ")
    asyncio.run(modifyCollection(response))
