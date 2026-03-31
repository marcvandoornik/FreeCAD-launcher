def sorted = new ArrayList(node.children).sort{ it['Name'].text }
sorted.eachWithIndex { it, i ->
    it.moveTo(node, i)
}
// @ExecutionModes({ON_SELECTED_NODE, ON_SELECTED_NODE_RECURSIVELY})