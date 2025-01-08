from fastapi import FastAPI

def create_app():
    return FastAPI(
        title='chat',
        docs_url='api/docs',
        description='new twitter'
    )