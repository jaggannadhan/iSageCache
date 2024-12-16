from flask import Blueprint, request, json
from flask import jsonify
from src.services.CacheService import CacheLLMResponseService

cache_handler = Blueprint("cache_handler", __name__)


@cache_handler.route("/get-top-queries", methods=["GET"])
def get_top_queries():
    k = request.args.get('k', 10)
    print(f"Requested queries: {k}")

    query_list, msg = CacheLLMResponseService.get_top_queries(k=k)
    return jsonify({
        "success": True,
        "query_list": query_list,
        "msg": msg
    })


@cache_handler.route("/cache-response", methods=["POST"])
def cache_query_response():
    data = json.loads(request.data)
    print(data)

    success, msg = CacheLLMResponseService.cache_query_response(data)
    return jsonify({
        "success": success,
        "msg": msg
    })