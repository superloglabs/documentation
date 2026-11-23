> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Documentation project instructions

## About this project

- This is a documentation site built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- Use the Mintlify MCP server, `https://mcp.mintlify.com`, to edit content and settings via MCP
- Use the Mintlify docs MCP server, `https://www.mintlify.com/docs/mcp`, to query information about using Mintlify via MCP

## Terminology

- The product is **Superlog**. The open-source repository is `superloglabs/responder-oss`; use the name Responder only when referring to that repository or to identifiers in it.
- A **finding** is a confirmed production problem that Superlog posts to Slack. Do not call the findings product by an internal name.
- An **automation** has **triggers**, **agent instructions**, **repositories**, **connectors**, a **model**, and a **harness**. One execution is a **run**.
- **Tag mode** answers Slack mentions. It is separate from automations.
- Use "workspace" for the tenant and "integration" for a connected tool.
- Positioning follows the landing page at superlog.sh: "Superlog scans your logs, finds the production issues your alerts miss, and posts each to Slack with its impact, root cause, and a suggested fix."
- Prices follow the pricing page at superlog.sh/pricing.

## Style preferences

- Plain, direct language. Short sentences. No marketing flourish.
- Use active voice and second person ("you")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references

## Content boundaries

- Document what the current code does. Check claims against `superloglabs/responder-oss` before publishing.
- Lead with findings. Document automations and tag mode as well. Do not document internal admin features.

## Credentials and customer data

- Never put credentials in commits, branch names, pull requests, issues, or
  review comments. This covers API keys, tokens, passwords, private keys,
  connection strings, and signed URLs. Refer to a secret by its name or where
  it is stored.
- Never put customer names or identifying details there either. This covers
  company and person names, emails, domains, organization and workspace IDs,
  and customer logs, traces, or error text. Describe the case in general terms
  and use made-up data in examples and screenshots.
