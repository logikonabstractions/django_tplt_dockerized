# dev version
ARG VERSION
FROM ${VERSION} 

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt

# using a bind mount so no need to copy
# COPY . .