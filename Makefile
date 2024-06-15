get_htmx:
	wget -P app/static/js https://unpkg.com/htmx.org@1.9/dist/htmx.min.js

all: get_htmx
