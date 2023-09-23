import Cocoa

let pasteboard = NSPasteboard.general
let customType = NSPasteboard.PasteboardType(rawValue: "com.runningwithcrayons.alfred.workflow.editor.prefab")

if let data = pasteboard.data(forType: customType) {
    if let str = String(data: data, encoding: .utf8) {
        print(str)
    }
}
