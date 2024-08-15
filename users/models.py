# from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo
# # Create your models here.
#
# # user model
# class Owner(StructuredNode):
#     uid = UniqueIdProperty()
#     username = StringProperty(unique_index=True, required=True)
#     # password = StringProperty()
#
# # Prompt model
# class Prompt(StructuredNode):
#     pid = UniqueIdProperty()
#     content = StringProperty(required=True)
#     owner = RelationshipTo(Owner, relation_type="Created by")
#
