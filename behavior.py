def update_cinderglade(card, context):
    if len(context.player.Board.TutorAll(["basic", "land"]).Cards) >= 2:
        card.RemoveTag("tapped")

def update_thornspire(card, context):
    if (context.player.Board.Tutor(["mountain", "land"]) or
        context.player.Board.Tutor(["forest", "land"])):
        card.AddTag("green")

def play_surveil(card, context):
    context.player.Strategy.Surveil(context)

def play_fetchland(card, context):
    if card.has_all_tags(["fetch_land","land"]):
        context.player.Strategy.FetchLand(context, card)
# Behavior maps
UPDATE_TAG_BEHAVIORS = {
    "cinderglade": update_cinderglade,
    "thornspire": update_thornspire,
}

PLAY_BEHAVIORS = {
    "surveil": play_surveil,
    "fetch_land": play_fetchland
}