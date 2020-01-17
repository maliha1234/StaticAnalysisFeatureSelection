library(ggplot2)

args <- commandArgs(trailing = TRUE)
folderName <- args[1]
programName <- args[2]
featureNumber <- args[3]
axislable<- args[4]

mydata <- read.table(folderName + programName + ".csv", header=TRUE, sep=",")

xC = ncol(mydata)

print(xC) 
for (c in featureNumber:featureNumber) 
{  
   for (c1 in 4:8)
{
     
      
       v1 <- mydata[[c]] # feature
       v2 <- mydata[[c1]] #configuration
       v3 <- mydata[[3]]  #time
      

      file_name <- paste("/Users/malihasarwat/Documents/Fall2019/ResearchPaperRepo/Feature-Analysis/ProjectDirectory/DataPlotWithRAllprograms/ALL/plot",colnames(mydata)[c],colnames(mydata)[c1],"data.jpg",sep="_")
      
      linecolors <- c("#F1370F", "#0F31F1", "#23BD3F")
      fillcolors <- c("#9D6C06", "#077DAA", "#23BD3F")
   
  myplot <-ggplot(mydata, aes(x= v3/1000, y= v1, color = v2, shape = factor(v2), alpha = 0.5))   + ylim(c(0,2000))  + geom_point() +  xlab("Time (Seconds)") + ylab(axislable) 
            
      ggsave(filename=file_name, plot=myplot,
       units = "cm" 
       )
      
    
    
 }
}