FROM nginx:latest

# remove existing/default nginx config file
RUN rm -f /etc/nginx/conf.d/default.conf

# copy our nginx config file to nginx config dir
COPY nginx.conf /etc/nginx/conf.d