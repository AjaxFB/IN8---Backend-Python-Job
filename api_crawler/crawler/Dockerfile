FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install -y python3-pip python3-dev build-essential
RUN cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
RUN apt-get install -y unzip curl
RUN apt-get install -y default-jdk 
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable
RUN wget https://chromedriver.storage.googleapis.com/78.0.3904.70/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver
COPY . /crawler
WORKDIR /crawler
RUN pip install -r requirements.txt
CMD python -u crawler.py

