
import traceback
from src.services.GoogleBucket import FileUploadService
from src.models.FAQModel import FAQ

class CacheLLMResponseService:

    CACHE_BUCKET = "isage-faq"
    
    def get_top_queries(self, k=10):
        try:
            query_list, msg = FAQ.get_all_queries(k)
            return query_list, msg
        except Exception:
            print(traceback.format_exc())
            return None
        
    def cache_query_response(self, data):
        try:
            query = data.get("query")
            answer = data.get("answer")

            blob_url, msg = FileUploadService.write_text_to_file(
                self.CACHE_BUCKET, 
                query, answer
            )
            print(msg)
            if blob_url:
                entity, msg = FAQ.add_query(query, blob_url)
                print(msg)
                return True, msg
        
            return False, msg
        except Exception:
            print(traceback.format_exc())
            return False, "Error occured in cache_query_response"