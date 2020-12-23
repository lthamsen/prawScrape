
import prawScrapeF as h

range_ = int(600)


posts = h.getSubData(range_,'all')

h.savePhotos(posts)