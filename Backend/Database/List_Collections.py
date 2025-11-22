from Custom_Chroma_Rag import AsyncChromaDB


async def list_collection():
    list_client = AsyncChromaDB()
    await list_client.client_init_async()
    client = list_client.client
    collections = await client.list_collections()
    return collections


if __name__ == "__main__":
    import asyncio

    result = asyncio.run(list_collection())
    print(result)
