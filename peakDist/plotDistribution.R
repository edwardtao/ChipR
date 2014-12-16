rm(list=ls())
args <- commandArgs(trailingOnly = TRUE)
datafiles <- args[1]
pics <- args[2]
picTile <- args[3]

data <- read.table(datafiles,header = F,sep='\t',stringsAsFactors =F)
mode(data) <- 'numeric'
data <- data[data>=-1000 & data <1000]
D <- data.frame(data=as.vector(data),con=factor(rep('A',length(data))))
# 
# distr <- cut(data,breaks = seq(-1000,1000,by=50))
# disD <- as.matrix(table(distr))
# n <- seq(-1000,1000,by=50)
# D <- data.frame(seq=n[-1],num=disD)
# plot(disD,type='s')

require(ggplot2)
require(splines)
library(scales)

Ag <- ggplot(D,aes(D$data)) 
ge <-  geom_bar(binwidth=50, colour="grey",fill='blue')
#ge <-  geom_bar(aes(y=..density..),,binwidth=20, colour="grey")
# AA <- Ag+ge+geom_density(fill="blue",alpha =0.6,weight=2)

btg <- labs(title =picTile)
Ab <- theme(plot.title=element_text(size = rel(2)),panel.background=element_blank())

gba <- xlim(-500, 500)
#gbb <- scale_x_discrete(breaks=seq(-500, 500, 50))#+scale_y_continuous(labels = p)
atg <- labs(x='Residue Distance',y='Peak Number')
abg <- theme(axis.text = element_text(colour = "black",size = rel(1.5)),axis.title=element_text(size = rel(2)),axis.line=element_line())
Ag+ge+btg+Ab+gba+atg+abg
#Ag+ge+gba+tg+theme(plot.title=element_text(size = rel(2)),axis.text = element_text(colour = "black",size = rel(1.5)),axis.title=element_text(size = rel(2)),panel.background=element_blank()
ggsave(filename=pics,plot=last_plot(),dpi=600)
