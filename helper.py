from urlextract import URLExtract

extract  = URLExtract()

def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch number of messages
    num_messages =  df.shape[0]
    # number of words in whatsapp chat 
    words = []
    for message in df['message']:
        words.extend(message.split())
    
    # fetch number of media messages 
    num_of_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    #  fetch number of links 
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    return num_messages, len(words) , num_of_media_messages ,len(links)



   