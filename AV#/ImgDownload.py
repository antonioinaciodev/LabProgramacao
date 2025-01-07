import os
import requests 

#todo fazer uma checagem de protocolo nos url
class Download:
    def __init__(self):
        self.output = "Download_output"
        if not os.path.exists(self.output):
            os.makedirs(self.output) #vai abrir uma pasta onde esse arquivi estiver 

    def download_img(self,url : str):
        try:
            arc_name = os.path.join(self.output,url.split("/")[-1]) 

            #download
            aux_response = requests.get(url).content
            
            with open(arc_name,"wb") as handler:
                handler.write(aux_response)

            print("imagem baixada")
            return arc_name
            
        except requests.exceptions.RequestException as e:
            print(f"erro ao fazer o download({e})")
            return None