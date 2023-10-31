from rest_framework.response import Response
from rest_framework.views import APIView
from recommendation_function import get_recommendation

class dt_recommender(APIView):
    def post(self, request, format=None):
        note = 'No Exception'
        label = ""
        status = 200
        try:
            request_data = request.data
            model_name = "decision_tree.pkl"
            label = get_recommendation(request_data, model_name)
            

        except Exception as e:
            note = str(e)
            status = 400
        return Response({'status':status,'note': note, 'recommendation': label}, status=status)
    
class nb_recommender(APIView):
    def post(self, request, format=None):
        note = 'No Exception'
        label = ""
        status = 200
        try:
            request_data = request.data
            model_name = "naive_bias.pkl"
            label = get_recommendation(request_data, model_name)
            

        except Exception as e:
            note = str(e)
            status = 400
        return Response({'status':status,'note': note, 'recommendation': label}, status=status)

