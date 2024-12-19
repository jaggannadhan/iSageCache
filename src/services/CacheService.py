
import traceback
from src.services.GoogleBucket import FileUploadService
from src.models.FAQModel import FAQ

class CacheLLMResponseService:

    CACHE_BUCKET = "isage-faq"
    
    @classmethod
    def get_top_queries(cls, k=20):
        try:
            print(f"get_top_queries service")
            query_list, msg = FAQ.get_all_queries(k)
            return query_list, msg
        except Exception:
            print(traceback.format_exc())
            return None, "Unable to connect to the DB"
        
    @classmethod
    def cache_query_response(cls, data):
        try:
            query = data.get("query")
            answer = data.get("answer")

            blob_url, msg = FileUploadService.write_text_to_file(
                cls.CACHE_BUCKET, 
                query, answer
            )
            print(msg)
            if blob_url:
                entity, msg = FAQ.add_query(query, blob_url)
                print(msg)
                return entity, msg
        
            return None, msg
        except Exception:
            print(traceback.format_exc())
            return False, "Error occured in cache_query_response"
        
    
    @classmethod
    def increment_query_vote(cls, data):
        try:
            query = data.get("query")
            FAQ.increment_vote_for_query(query)
            return True, "Sucessfully incremented vote for query"
        except Exception:
            print(traceback.format_exc())
            return False, "Error occured in increment_query_vote"