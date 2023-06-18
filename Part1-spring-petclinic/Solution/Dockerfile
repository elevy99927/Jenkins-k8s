#######################
# Builder
#######################
From eclipse-temurin:20.0.1_9-jdk-alpine as builder

#RUN mkdir /app
WORKDIR /app
COPY . .
RUN ./mvnw package

##########################
# Run Time
#########################
FROM eclipse-temurin:17-jdk-alpine as server

#Copy all files from /target/*.jar from step 2 TO /code
WORKDIR /code
COPY --from=builder /app/target/*.jar /code
RUN chmod a+rx /code -R

#Make sure your CMD is:  java -jar code/*.jar
CMD ["java", "-jar", "/code/spring-petclinic-3.1.0-SNAPSHOT.jar"]


