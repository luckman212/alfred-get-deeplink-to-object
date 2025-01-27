![](./icon.png)

## Alfred Deeplink

Little helper workflow to get a deeplink to a specific workflow object in Alfred 5. A deeplink in this case represents a link that uses Alfred's `alfredpreferences://` URI scheme to open the Workflow Editor directly to a specific Workflow, with a specific Object highlighted. This might be useful, especially to developers, for keeping notes or internal documentation about specific Workflows you're working on.

### To use

Highlight a workflow object, press ⌘C, then activate this workflow (default hotkey trigger is ⇧⌘C). The URI will be copied to the clipboard.

Once you have your URI, you can use it (for example) like this:

```shell
open 'alfredpreferences://navigateto/workflows>workflow>user.workflow.21367E91-3165-4B5C-858B-E3DA84B8F111>E3703BDE-5F15-427E-9A3E-1EB5FDEACFAE'
```

### Related forum thread

https://www.alfredforum.com/topic/18390-get-currently-edited-workflow-uri/

### Requirements

- Python3 (Comes with Xcode, or you can install with Homebrew)
- Alfred 5.1 or higher
