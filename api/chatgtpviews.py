class FamilyList(generics.ListAPIView):
    serializer_classes = {
        'history': FamilySerializerHistory,
        'crest': FamilySerializerCrest,
        'prdImages': FamilySerializerProducts,
        'historyandcrests': FamilySerializerHistoryCrest,
        'crestandproducts': FamilySerializerProductsCrest,
        'historyandproducts': FamilySerializerHistoryProd,
        'default': FamilySerializerGeneral,
    }

    def get_serializer_class(self):
        query_params = self.request.query_params
        serializer_class = self.serializer_classes.get('default')

        if query_params.get('history'):
            serializer_class = self.serializer_classes.get('history')
        elif query_params.get('crest'):
            serializer_class = self.serializer_classes.get('crest')
        elif query_params.get('prdImages'):
            serializer_class = self.serializer_classes.get('prdImages')
        elif query_params.get('history') and query_params.get('crest'):
            serializer_class = self.serializer_classes.get('historyandcrests')
        elif query_params.get('crest') and query_params.get('prdImages'):
            serializer_class = self.serializer_classes.get('crestandproducts')
        elif query_params.get('history') and query_params.get('prdImages'):
            serializer_class = self.serializer_classes.get('historyandproducts')

        return serializer_class

    def get_queryset(self):
        queryset = Family.objects.all()
        name = self.request.query_params.get('name')
        queryset = queryset.filter(name=name)

        return queryset
    


    #### ESTE ES EL QUE VA EL DE ACA ABAJO ES GOD

    class MyView(APIView):
    def get(self, request):
        context_var = request.GET.get('context_var')

        # Pass the context variable when instantiating the serializer
        serializer = FamilySerializerGeneral(Family.objects.all(), many=True, context={'context_var': context_var})
        data = serializer.data

        return Response(data)
    


    ##############################3

    