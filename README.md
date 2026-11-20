# Superlog documentation

Source for [docs.superlog.sh](https://docs.superlog.sh), built with [Mintlify](https://mintlify.com).

Superlog scans your logs, finds the production issues your alerts miss, and posts each to Slack with its impact, root cause, and a suggested fix. The open-source application code is at [superloglabs/responder-oss](https://github.com/superloglabs/responder-oss).

## Preview locally

```bash
npm i -g mint
mint dev
```

Open `http://localhost:3000`.

## Check links

```bash
mint broken-links
```

## Publish

Changes deploy automatically after they are merged to `main`.
