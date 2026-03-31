<map version="freeplane 1.12.15">
<!--To view this file, download free mind mapping software Freeplane from https://www.freeplane.org -->
<attribute_registry SHOW_ATTRIBUTES="selected">
    <attribute_name VISIBLE="true" NAME="Name"/>
    <attribute_name VISIBLE="true" NAME="Value"/>
</attribute_registry>
<bookmarks/>
<node TEXT="FCParameters" FOLDED="false" ID="ID_961418806" CREATED="1769694541275" MODIFIED="1769694541275"><hook NAME="MapStyle" background="#ffffffff">
    <properties show_icon_for_attributes="false" show_tags="UNDER_NODES" show_note_icons="true" fit_to_viewport="false" show_icons="BESIDE_NODES" showTagCategories="false"/>
    <tags category_separator="::"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="bottom_or_right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ID="ID_1981748968" ICON_SIZE="12 pt" FORMAT_AS_HYPERLINK="false" COLOR="#7f7f7f" BACKGROUND_COLOR="#ffcc00" BACKGROUND_ALPHA="0" STYLE="fork" SHAPE_HORIZONTAL_MARGIN="3 px" SHAPE_VERTICAL_MARGIN="2 px" NUMBERED="false" FORMAT="NO_FORMAT" TEXT_ALIGN="CENTER" TEXT_WRITING_DIRECTION="LEFT_TO_RIGHT" MAX_WIDTH="200 px" MIN_WIDTH="200 px" VGAP_QUANTITY="2 px" COMMON_HGAP_QUANTITY="14 pt" CHILD_NODES_LAYOUT="AUTO" BORDER_WIDTH_LIKE_EDGE="false" BORDER_WIDTH="1 px" BORDER_COLOR_LIKE_EDGE="true" BORDER_COLOR="#808080" BORDER_DASH_LIKE_EDGE="false" BORDER_DASH="SOLID">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" DASH="" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1981748968" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<font NAME="Arial" SIZE="8" BOLD="false" UNDERLINED="false" STRIKETHROUGH="false" ITALIC="true"/>
<richcontent TYPE="DETAILS" CONTENT-TYPE="plain/html"/>
<richcontent TYPE="NOTE" CONTENT-TYPE="plain/html"/>
<edge STYLE="linear" COLOR="#cccccc"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.tags">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" BACKGROUND_COLOR="#ffffff"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.selection" BACKGROUND_COLOR="#4e85f8" BORDER_COLOR_LIKE_EDGE="false" BORDER_COLOR="#4e85f8"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes" COLOR="#000000" BACKGROUND_COLOR="#ffdccb" BORDER_COLOR="#808080" BORDER_COLOR_ALPHA="0">
<font SIZE="8" ITALIC="false"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="bottom_or_right" STYLE="bubble"/>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="bottom_or_right" STYLE="bubble"/>
</stylenode>
</map_styles>
</hook>
<node TEXT="SORTING SCRIPT" POSITION="top_or_left" ID="ID_1951394763" CREATED="1770128252790" MODIFIED="1770128303160">
<attribute NAME="script1" VALUE="def sorted = new ArrayList(node.children).sort{ it[&apos;Name&apos;].text }&#xd;&#xa;sorted.eachWithIndex { it, i -&gt;&#xd;&#xa;    it.moveTo(node, i)&#xd;&#xa;}&#xd;&#xa;// @ExecutionModes({ON_SELECTED_NODE, ON_SELECTED_NODE_RECURSIVELY})"/>
</node>
</node>
</map>
