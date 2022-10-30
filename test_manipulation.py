from app.db.manipulation import get_nearest
from app.models.data_transfer_models import *

def test_get_nearest():
    out = get_nearest(51.5074, 0.1278)
    assert isinstance(out, HandshakeOut)
    assert isinstance(out.stories, list)
    assert isinstance(out.stories[0], Story)
    assert out.stories[0].story_id == 1
