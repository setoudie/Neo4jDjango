from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo

# Modèle pour les Owners
class Owner(StructuredNode):
    uid = UniqueIdProperty()
    username = StringProperty(unique_index=True, required=True)
    # password = StringProperty()  # Décommente si tu souhaites stocker les mots de passe

# Modèle pour les Prompts
class Prompt(StructuredNode):
    pid = UniqueIdProperty()
    content = StringProperty(required=True)
    owner = RelationshipTo(Owner, 'Created by')  # Relation avec le modèle Owner
