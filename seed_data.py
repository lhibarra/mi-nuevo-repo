from SocialTravel.models import Post
# Post(carousel_caption_title= "Un carousel title",
#      carousel_caption_description="Un carousel descript",
#      heading = "un viaje",
#     description = "Una dewscripcion",
# ).save()

for _ in range(0, 1000):
    Post(carousel_caption_title="Un Carousel Title",
         carousel_caption_description="Un carousel descript",
         heading="Mi viaje",
         description="una description",
         un_campo=""
         ).save()
