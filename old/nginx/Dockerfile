FROM nginx:latest

# Adding custom index.html hosted on Github Gist
COPY index.html /usr/share/nginx/html/index.html

# Adding read permissions to custom index.html
RUN chmod +r /usr/share/nginx/html/index.html

CMD ["nginx", "-g", "daemon off;"]
