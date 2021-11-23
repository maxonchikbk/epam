FROM alpine:latest as build-stage
RUN apk add npm --no-cache
COPY ./app /app
WORKDIR /app
RUN  npm install && npx browserslist@latest --update-db && npm run build

FROM alpine:latest
COPY --from=build-stage /app/build /build
RUN apk add npm --no-cache && npm install -g serve
EXPOSE 3000
ENTRYPOINT [ "serve" ]
CMD ["-s", "build"]