import os
import requests 

class Download:
    def __init__(self,path = None):
        self.output = path
        
    def download_img(self,url : str):
        if not self.output :
            return "Diretorio não especificado"
         
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