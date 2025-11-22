from Custom_Chroma_Rag import AsyncChromaDB


async def checkCollection(collection_name: str = "Default"):
    if collection_name=='Default':
        raise RuntimeError("Default collection can't be initialized, please pass collection_name")
    clientDetails = AsyncChromaDB(collection_name=collection_name)
    await clientDetails.client_init_async()
    print(collection_name)
    count=await clientDetails.collection.count()
    peek=await clientDetails.collection.peek()
    print(f"✅ Collection --> {collection_name} number of records in the collection is {count}. \n")
    print(f"✅ Collection --> {collection_name} first 10 records in the collection is {peek}. \n")


if __name__ == "__main__":
    import asyncio
    response=input("Type your collection name to see details: ")
    asyncio.run(checkCollection(response))
