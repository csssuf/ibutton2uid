FROM python:3-alpine
MAINTAINER James Forcier "csssuf@csssuf.net"

EXPOSE 8080

COPY . /app
WORKDIR /app

RUN apk upgrade --no-cache && \
apk add --no-cache python-dev gcc musl-dev openssl-dev openldap-dev ca-certificates && \
update-ca-certificates

RUN echo "tls_cacertdir /etc/ssl/certs" >> /etc/openldap/ldap.conf

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python"]
CMD ["ibutton2uid.py"]
