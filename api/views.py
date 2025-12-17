from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer
from .services import generate_answer

class FAQListCreate(APIView):
    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FAQDetail(APIView):
    def get(self, request, id):
        faq = FAQ.objects.get(id=id)
        serializer = FAQSerializer(faq)
        return Response(serializer.data)


class AISuggestAnswer(APIView):
    def post(self, request):
        question = request.data.get('question')
        answer = generate_answer(question)
        return Response({"draft_answer": answer})
