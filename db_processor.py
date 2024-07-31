import os
from dotenv import load_dotenv
from supabase import create_client, Client

#env 파일 불러오기
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv()
 
#환경변수
url=os.getenv('SUPABASE_URL')
key=os.getenv('SUPABASE_KEY')

#Type hinting: 명시적으로 데이터 타입을 설명해줌, 여기서 데이터 타입은 Client
supabase: Client = create_client(url, key)

#DB)article 테이블에 insert
def insert_into_articles(article):
    response = (
        supabase.table('articles').insert({
            "title": article["title"],
            "link": article["link"]
        }).execute()
    )

    inserted_row = response.data[0]
    generated_uuid=inserted_row['id']

    return generated_uuid