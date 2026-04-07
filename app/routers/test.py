from fastapi import APIRouter
from supabase import create_client

router = APIRouter(prefix="/test", tags=["Test"])

# 👉 Supabase 정보 넣기
url = "https://rnicbviddcyabtbcrsmh.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJuaWNidmlkZGN5YWJ0YmNyc21oIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ0MzAyOTgsImV4cCI6MjA5MDAwNjI5OH0.2n6SdjVwmrMigecgZq6SOgVaqSYd1yvJtUYQqooTJoI"

supabase = create_client(url, key)


# ✅ 게시글 전체 조회
@router.get("/posts")
def get_posts():
    data = supabase.table("posts").select("*").execute()
    return data.data


# ✅ 게시글 생성
@router.post("/posts")
def create_post(user_id: str, title: str, content: str):
    data = supabase.table("posts").insert({
        "user_id": user_id,
        "title": title,
        "content": content
    }).execute()
    return data.data