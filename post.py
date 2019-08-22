from steem import Steem

def post(username, wif, title, body, permlink=None, reply_identifier=None, json_metadata=None, comment_options=None, community=None, tags=None, beneficiaries=None, self_vote=False):
    s = Steem(keys=wif,
                  nodes=["https://api.steemit.com", "https://rpc.buildteam.io"])
    s.commit.post(title, body, username, permlink, reply_identifier, json_metadata, comment_options, community, tags, beneficiaries, self_vote)

# example :

post("username", "posting key" ,title="Python Test", body="blank", tags=['spam','test'], self_vote=False)
