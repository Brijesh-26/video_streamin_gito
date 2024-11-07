FROM python:3.10-slim as base

FROM base AS python-deps 

RUN apt update && apt install bash gcc git -y && pip install --upgrade pip

COPY requirements.txt .
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt --prefer-binary
COPY .git/HEAD .
RUN mv HEAD git-commit.txt


FROM base AS runtime
COPY --from=python-deps /.venv /.venv
ENV PATH /.venv/bin:$PATH

RUN apt update && apt install -y wkhtmltopdf

RUN adduser --disabled-password appuser
WORKDIR /home/appuser
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
USER appuser

COPY . .
RUN mkdir logs
COPY --from=python-deps git-commit.txt .
EXPOSE 8000
ENTRYPOINT [ "./entrypoint.sh" ]

