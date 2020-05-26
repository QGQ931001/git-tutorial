library(sf)
library(readr)
library(tidyverse)
library(hrbrthemes)
# install.packages("https://czxa.top/pkg/ggtext_0.1.0.tar.gz", repos = NULL, type = "source")
library(ggtext)
# 世界地图数据
setwd("/home/qgq/文档/大城市发展的有多快")
worldmap <- read_sf('world.geo.json') %>% 
  st_transform(crs = 4326)


read_csv('data-bKvwd.csv')->df
names(df)


read_csv('data-bKvwd.csv') %>% 
  st_as_sf(coords = c("Lon", "Lat"), crs = 4326) %>% 
  select(`2000-2016`, category, geometry) %>% 
  mutate(`2000-2016` = as.numeric(`2000-2016`)) -> df

ggplot(worldmap) + 
  geom_sf(size = 0.1, color = "black", 
          fill = "#F3F3F3") + 
  geom_sf(data = df, aes(size = `2000-2016` + 1, 
                         color = category),
          alpha = 0.5) + 
  theme_ipsum(base_family = cnfont,
              subtitle_family = cnfont,
              caption_family = cnfont,
              grid = "") + 
  worldtilegrid::theme_enhance_wtg() + 
  scale_size_continuous(range = c(1, 5)) + 
  scale_color_manual(values = c("negative" = "#FDAB62",
               "between 0 and 2.5" = "#9CDAE6",
               "between 2.5 and 5" = "#189DB6",
               "5 or more" = "#244C6A",
               "null" = NA)) + 
  theme(legend.position = "none", 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank()) + 
  labs(title = "大城市发展的有多快？",
       subtitle = "该图展示了 2016 年所有人口超过 100 万的大城市，圆圈的大小和颜色表示 2000 年到 2016 年间城市人口的平均增长速度。<b><span style='color:\"#FDAB62\"'>负增长</span>/<span style='color:\"#9CDAE6\";'>0 - 2.5%</span>/<span style='color:\"#189DB6\";'>2.5% - 5%</span>/<span style='color:\"#244C6A\";'>超过 5%</span></b>",
       caption = "数据来源: How fast do big cities grow? | Created with Datawrapper\n<https://www.datawrapper.de/_/bKvwd/>\n绘制：TidyFriday") + 
  theme(plot.subtitle = element_textbox_simple()) + 
  coord_sf(crs = "+proj=eck4")





download.file("https://czxa.top/pkg/world.geo.json", "world.geo.json")