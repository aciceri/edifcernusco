SHELL=bash
ftp-host = ftp.edifcernusco.it
ftp-user = 9661326@aruba.it
ftp-pass = 6dGl5qAc59
ftp-path = www.edifcernusco.it/demo2/

server:
	cd site && python2 -m SimpleHTTPServer 8080 /site/

clean:
	rm -Rf minified/*

minify:
	rm -Rf minified/*
	cp site/statuto.pdf minified/statuto.pdf
	cp site/send.php minified/send.php
	mkdir minified/images
	mkdir minified/images/realizzazioni
	cp -R site/images/* minified/images/
	mkdir minified/assets
	mkdir minified/assets/css
	postcss site/assets/css/ --dir minified/assets/css/
	mkdir minified/assets/js
	cp site/assets/js/{breakpoints.min.js,browser.min.js,jquery.min.js,jquery.scrollex.min.js} minified/assets/js/
	uglifyjs site/assets/js/main.js > minified/assets/js/main.js
	uglifyjs site/assets/js/util.js > minified/assets/js/util.js	
	mkdir minified/assets/fonts
	cp site/assets/fonts/* minified/assets/fonts/
	html-minifier --collapse-whitespace --remove-comments --remove-optional-tags --remove-redundant-attributes --remove-script-type-attributes --remove-tag-whitespace --use-short-doctype site/index.html -o minified/index.html

deploy:
	make minify
	ncftpput -R -v -u $(ftp-user) -p $(ftp-pass) $(ftp-host) $(ftp-path) minified/*
