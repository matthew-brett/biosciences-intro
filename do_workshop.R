calibration = read.table('calibration.csv')
calibration
calibration = read.csv('calibration.csv')
calibration
plot(Absorbance ~ BSA, data=calibration)
model = lm(Absorbance ~ BSA, data=calibration)
fit = fit(model)
model
fit = lm(Absorbance ~ BSA, data=calibration)
abline(fit)
predict(fit, 0.25)

plot(Absorbance ~ BSA, data=calibration, title='Foo')
plot(Absorbance ~ BSA, data=calibration, main='Foo')
plot(Absorbance ~ BSA, data=calibration, main='BSA vs Absorbance')
0.25 / fit$beta
fit$beta
fit$coefficients
fit$coefficients[1]
fit$coefficients[2]
abline(fit)
bathing = read.csv('bathing.csv')
bar
barv
bathing
barplot?
help(barplot)
help(barplot)
barplot(bathing$Average.Number.of.coliforms.in.100ml.sea.water)
bathing$Average.Number.of.coliforms.in.100ml.sea.water
bathing
help(bathing)
str(bathing)
bathing = read.csv('bathing.csv')
bathing
str(bathing)
bathing = read.csv('bathing.csv')
bathing
barplot(bathing$Average.Number.of.coliforms.in.100ml.sea.water)
help(read.csv)
bathing = read.csv('bathing.csv')
bathing
barplot(bathing$Average.Number.of.coliforms.in.100ml.sea.water_
barplot(bathing$Average.Number.of.coliforms.in.100ml.sea.water)
barplot(bathing$Average.Number.of.coliforms.in.100ml.sea.water)
barplot(bathing)
barplot(bathing[1])
bathing[1]
barplot(as.matrix(bathing))
barplot(as.matrix(bathing[1]))
bathing = read.csv('bathing.csv')
barplot(bathing$Average.Number.of.coliforms.in.100ml.sea.water, names=bathing$Bathing.Waters)
barplot(bathing$Average.Number.of.coliforms.in.100ml.sea.water, names=bathing$Bathing.Waters, las=2)
barx = barplot(bathing$Average.Number.of.coliforms.in.100ml.sea.water, names=bathing$Bathing.Waters, las=2)
barx
coliforms = bathing$Average.Number.of.coliforms.in.100ml.sea.water
coliforms_sd = bathing$StDev
names = bathing$Bathing.Waters
barplot(coliforms, names=names)
barplot(coliforms, names=names, las=2)
x_positions = barplot(coliforms, names=names, las=2)
barplot(x0=x_positions, y0=coliforms+coliforms_sd)
arrows?
help(arrows)
barplot(x0=x_positions, y0=coliforms, x1=x_positions, y1=coliforms+coliforms_sd)
help(arrows)
barplot(x0=x_positions, y0=coliforms, x1=x_positions, y1=coliforms+coliforms_sd, angle=90,code=3,length=0.1)
arrows(x0=x_positions, y0=coliforms, x1=x_positions, y1=coliforms+coliforms_sd, angle=90,code=3,length=0.1)
arrows(x0=x_positions, y0=coliforms-coliforms_sd, x1=x_positions, y1=coliforms+coliforms_sd, angle=90,code=3,length=0.1)
barplot(coliforms, names=names, las=2, border=NA)
arrows(x0=x_positions, y0=coliforms-coliforms_sd, x1=x_positions, y1=coliforms+coliforms_sd, angle=90,code=3,length=0.1)
height_weight = read.csv('height_weight.csv')
height_weight
height_weight = read.csv('height_weight.csv')
height_weight
bind(height_weight)
cbind(height_weight)
height
bmi = height_weight$weight / height_weight$weight ^ 2
bmi
hist(bmi)
table(bmi)
describe(height_weight)
summary(height_weight)
history()
savehistory(file='do_workshop.R')
