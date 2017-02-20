import datetime
from haystack import indexes
from shop.models import ModifiedProduct


class ModifiedProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    

    def get_model(self):
        return ModifiedProduct

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(updated__lte=datetime.datetime.now())
