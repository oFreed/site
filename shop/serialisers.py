from django_elastic_appsearch import serialisers


class CategorySerialiser(serialisers.AppSearchSerialiser):
    name = serialisers.StrField()


class ProductSerialiser(serialisers.AppSearchSerialiser):
    brand = serialisers.StrField()
    model = serialisers.StrField()
    price = serialisers.Field()
    category_id = serialisers.MethodField()

    def get_category_id(self, instance):
        return '{}'.format(
            instance.category.id
        )

