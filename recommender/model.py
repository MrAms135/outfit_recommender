import random
def recommend_outfit(user_input,outfit_data):
    filtered=outfit_data[outfit_data['occasion']==user_input['occasion']]
    if filtered.empty:
        return "No outfit found for this occasion"
    return filtered.sample(1).iloc[0]