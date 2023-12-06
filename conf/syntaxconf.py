import re
import tkinter as tk
import editortheme as et
#C Language --> index 0
CExtensionsList = [".c", ".h", ".cpp", ".hpp", ".inc"]
Cregex = re.compile(
        r"(^\s*"
        r"(?P<if>\bif\b)" + "|"  # if condition
        r"(?P<for>\bfor\b)" + "|"  # for loop
        r"(?P<while>\bwhile\b)" + "|"  # while loop
        r"(?P<include>#include\s+[\"<]\S+)" + "|"
        r"(?P<int>\bint\b)" + "|"   # int variable
        r"(?P<float>\bfloat\b)" + "|" #float variable
        r"(?P<char>\bchar\b)" + "|" #char variable
        r"(?P<number>\b[0-9]+)" + "|" #numbers
        r"(?P<plusOperator>[\+]+)" + "|" #plusOperator
        r"(?P<minusOperator>[\-]+)" + "|" #minusOperator
        r"(?P<multOperator>[\*]+)" + "|" #multOperator
        r"(?P<divOperator>[\/]+)" + "|" #divOperator
        r"(?P<equalOperator>[=]+)" + "|" #equalOperator
        r"(?P<return>\breturn\b)" +  #return
        r"[\s\(]+)"
    )
def applyC_Tags(code):
    lines = code.text.get(1.0, tk.END).splitlines()
    for idx, line in enumerate(lines):
        int_tag = f"int_{idx}"
        float_tag = f"float_{idx}"
        char_tag = f"char_{idx}"
        for_tag = f"for_{idx}"
        while_tag = f"while_{idx}"
        if_tag = f"if_{idx}"
        include_tag = f"include_{idx}"
        number_tag = f"number_{idx}"
        plusOperator_tag = f"plusOperator_{idx}"
        minusOperator_tag = f"minusOperator_{idx}"
        multOperator_tag = f"multOperator_{idx}"
        divOperator_tag = f"divOperator_{idx}"
        equalOperator_tag = f"equalOperator_{idx}"
        return_tag = f"return_{idx}"
        tags = {}
        if et.SelectedTheme == et.DefaultTheme:
            tags = {
                int_tag: "blue",
                float_tag: "blue",
                char_tag: "blue",
                for_tag: "green",
                while_tag: "green",
                if_tag: "purple",
                include_tag: "green",
                number_tag: "red",
                plusOperator_tag: "green",
                minusOperator_tag: "green",
                multOperator_tag: "green",
                divOperator_tag: "green",
                equalOperator_tag: "#b5179e",
                return_tag: "blue"
                # add new tag here
            }
        else:
            tags = {
                int_tag: "#6B6BBC",
                float_tag: "#6B6BBC",
                char_tag: "#6B6BBC",
                for_tag: "orange",
                while_tag: "orange",
                if_tag: "orange",
                include_tag: "green",
                number_tag: "orange",
                plusOperator_tag: "#fb8500",
                minusOperator_tag: "#fb8500",
                multOperator_tag: "#fb8500",
                divOperator_tag: "#fb8500",
                equalOperator_tag: "#2a9d8f",
                return_tag: "orange"
                # add new tag here
        }
        code._configure_tags(code.text, tags)
        for match in Cregex.finditer(line):     #substitute here the proper regex variable!
            for tag in tags:
                group_name = tag.split("_")[0]
                if -1 != match.start(group_name):
                    code.text.tag_add(
                        tag,
                        "{0}.{1}".format(idx+1, match.start(group_name)),
                        "{0}.{1}".format(idx+1, match.end(group_name))
                    )


#Python Language --> index 1
PyExtensionsList = [".py"]
Pyregex = re.compile(
    r"(^\s*"
    r"(?P<if>\bif\b)" + "|"  # if condition
    r"(?P<for>\bfor\b)" + "|"  # for loop
    r"(?P<import>\bimport\b)" + "|"
    r"(?P<return>\breturn\b)" +  "|" #return
    r"(?P<True>\bTrue\b)" + "|" #True
    r"(?P<False>\bFalse\b)" + "|" #False
    r"(?P<number>\b[0-9]+)" + "|" #numbers
    r"(?P<plusOperator>[\+]+)" + "|" #plusOperator
    r"(?P<minusOperator>[\-]+)" + "|" #minusOperator
    r"(?P<multOperator>[\*]+)" + "|" #multOperator
    r"(?P<divOperator>[\/]+)" + "|" #divOperator
    r"(?P<equalOperator>[=]+)" + "|" #equalOperator
    r"(?P<CommentedLine>#.*)" + "|" #commented line
    r"(?P<stringQuotes>'.*')" + "|" #stringQuotes
    r'(?P<stringDoubleQuotes>".*")' + "|" #stringDoubleQuotes
    r'(?P<underlinedName>__name__)' + "|" #underlined names
    r"(?P<def>\bdef\b)" + #def
    r"[\s\(]+)"
    )
def applyPy_Tags(code):
    lines = code.text.get(1.0, tk.END).splitlines()
    for idx, line in enumerate(lines):
        for_tag = f"for_{idx}"
        if_tag = f"if_{idx}"
        import_tag = f"import_{idx}"
        return_tag = f"return_{idx}"
        def_tag = f"def_{idx}"
        True_tag = f"True_{idx}"
        False_tag = f"False_{idx}"
        number_tag = f"number_{idx}"
        plusOperator_tag = f"plusOperator_{idx}"
        minusOperator_tag = f"minusOperator_{idx}"
        multOperator_tag = f"multOperator_{idx}"
        divOperator_tag = f"divOperator_{idx}"
        equalOperator_tag = f"equalOperator_{idx}"
        CommentedLine_tag = f"CommentedLine_{idx}"
        stringQuotes_tag = f"stringQuotes_{idx}"
        underlinedName_tag = f"underlinedName_{idx}"
        stringDoubleQuotes_tag = f"stringDoubleQuotes_{idx}"
        tags = {}
        if et.SelectedTheme == et.DefaultTheme:
            tags = {
                for_tag: "blue",
                if_tag: "blue",
                import_tag: "purple",
                return_tag: "blue",
                def_tag: "blue",
                True_tag: "red",
                False_tag: "red",
                CommentedLine_tag: "gray",
                stringQuotes_tag: "green",
                stringDoubleQuotes_tag: "green",
                underlinedName_tag: "#ff7900",
                number_tag: "#ff7900",
                plusOperator_tag: "red",
                minusOperator_tag: "red",
                multOperator_tag: "red",
                divOperator_tag: "red",
                equalOperator_tag: "red",
                # add new tag here
            }
        else:
            tags = {
            for_tag: "orange",
            if_tag: "orange",
            import_tag: "orange",
            return_tag: "orange",
            def_tag: "orange",
            True_tag: "red",
            False_tag: "red",
            CommentedLine_tag: "gray",
            stringQuotes_tag: "green",
            stringDoubleQuotes_tag: "green",
            underlinedName_tag: "#ff7900",
            number_tag: "#ff7900",
            plusOperator_tag: "red",
            minusOperator_tag: "red",
            multOperator_tag: "red",
            divOperator_tag: "red",
            equalOperator_tag: "red",
            # add new tag here
        }
        code._configure_tags(code.text, tags)
        for match in Pyregex.finditer(line):     #substitute here the proper regex variable!
            for tag in tags:
                group_name = tag.split("_")[0]
                if -1 != match.start(group_name):
                    code.text.tag_add(
                        tag,
                        "{0}.{1}".format(idx+1, match.start(group_name)),
                        "{0}.{1}".format(idx+1, match.end(group_name))
                    )

#VHDL language
VHDLExtensionsList = [".vhd"]
VHDLregex = re.compile(
    r"(^\s*"
    r"(?P<if>\bif\b)" + "|"  # if condition
    r"(?P<for>\bfor\b)" + "|"  # for loop
    r"(?P<entity>\bentity\b)" +  "|" #entity
    r"(?P<architecture>\barchitecture\b)" + "|" #architecture
    r"(?P<of>\bof\b)" + "|" #of
    r"(?P<is>\bis\b)" + "|" #is
    r"(?P<use>\buse\b)" + "|" #use
    r"(?P<library>\blibrary\b)" + "|" #library
    r"(?P<generate>\bgenerate\b)" + "|" #generate
    r"(?P<in>\bin\b)" + "|" #in
    r"(?P<out>\bout\b)" + "|" #out
    r"(?P<to>\bto\b)" + "|" #to
    r"(?P<downto>\bdownto\b)" + "|" #downto
    r"(?P<port>\bport\b)" + "|" #port
    r"(?P<map>\bmap\b)" + "|" #map
    r"(?P<generic>\bgeneric\b)" + "|" #generic
    r"(?P<begin>\bbegin\b)" + "|" #begin
    r"(?P<end>\bend\b)" + "|" #end
    r"(?P<process>\bprocess\b)" + "|" #process
    r"(?P<number>\b[0-9]+)" + "|" #numbers
    r"(?P<plusOperator>[\+]+)" + "|" #plusOperator
    r"(?P<minusOperator>[\-]+)" + "|" #minusOperator
    r"(?P<multOperator>[\*]+)" + "|" #multOperator
    r"(?P<divOperator>[\/]+)" + "|" #divOperator
    r"(?P<equalOperator>[=]+)" + "|" #equalOperator
    r"(?P<CommentedLine>#.*)" + "|" #commented line
    r"(?P<stringQuotes>'.*')" + "|" #stringQuotes
    r'(?P<stringDoubleQuotes>".*")' + "|" #stringDoubleQuotes
    r"[\s\(]+)"
    , re.IGNORECASE)

def applyVHDL_Tags(code):
    lines = code.text.get(1.0, tk.END).splitlines()
    for idx, line in enumerate(lines):
        for_tag = f"for_{idx}"
        if_tag = f"if_{idx}"
        entity_tag = f"entity_{idx}"
        of_tag = f"of_{idx}"
        is_tag = f"is_{idx}"
        use_tag = f"use_{idx}"
        library_tag = f"library_{idx}"
        generate_tag = f"generate_{idx}"
        in_tag = f"in_{idx}"
        out_tag = f"out_{idx}"
        to_tag = f"to_{idx}"
        downto_tag = f"downto_{idx}"
        port_tag = f"port_{idx}"
        map_tag = f"map_{idx}"
        generic_tag = f"generic_{idx}"
        begin_tag = f"begin_{idx}"
        end_tag = f"end_{idx}"
        process_tag = f"process_{idx}"
        architecture_tag = f"architecture_{idx}"
        number_tag = f"number_{idx}"
        plusOperator_tag = f"plusOperator_{idx}"
        minusOperator_tag = f"minusOperator_{idx}"
        multOperator_tag = f"multOperator_{idx}"
        divOperator_tag = f"divOperator_{idx}"
        equalOperator_tag = f"equalOperator_{idx}"
        CommentedLine_tag = f"CommentedLine_{idx}"
        stringQuotes_tag = f"stringQuotes_{idx}"
        stringDoubleQuotes_tag = f"stringDoubleQuotes_{idx}"
        tags = {}
        if et.SelectedTheme == et.DefaultTheme:
            tags = {
                for_tag: "blue",
                if_tag: "blue",
                entity_tag: "blue",
                of_tag: "blue",
                is_tag: "blue",
                architecture_tag: "blue",
                use_tag: "red",
                library_tag: "red",
                generate_tag: "red",
                in_tag: "red",
                out_tag: "red",
                to_tag: "red",
                downto_tag: "blue",
                port_tag: "blue",
                map_tag: "blue",
                generic_tag: "blue",
                begin_tag: "red",
                end_tag: "red",
                process_tag: "blue",
                CommentedLine_tag: "gray",
                stringQuotes_tag: "purple",
                stringDoubleQuotes_tag: "purple",
                number_tag: "red",
                plusOperator_tag: "purple",
                minusOperator_tag: "purple",
                multOperator_tag: "purple",
                divOperator_tag: "purple",
                equalOperator_tag: "purple",
                # add new tag here
            }
        else:
            tags = {
                for_tag: "blue",
                if_tag: "blue",
                entity_tag: "blue",
                of_tag: "blue",
                is_tag: "blue",
                architecture_tag: "blue",
                use_tag: "red",
                library_tag: "red",
                generate_tag: "red",
                in_tag: "red",
                out_tag: "red",
                to_tag: "red",
                downto_tag: "blue",
                port_tag: "blue",
                map_tag: "blue",
                generic_tag: "blue",
                begin_tag: "red",
                end_tag: "red",
                process_tag: "blue",
                CommentedLine_tag: "gray",
                stringQuotes_tag: "purple",
                stringDoubleQuotes_tag: "purple",
                number_tag: "red",
                plusOperator_tag: "purple",
                minusOperator_tag: "purple",
                multOperator_tag: "purple",
                divOperator_tag: "purple",
                equalOperator_tag: "purple",
                # add new tag here
            }

        code._configure_tags(code.text, tags)
        for match in VHDLregex.finditer(line):     #substitute here the proper regex variable!
            for tag in tags:
                group_name = tag.split("_")[0]
                if -1 != match.start(group_name):
                    code.text.tag_add(
                        tag,
                        "{0}.{1}".format(idx+1, match.start(group_name)),
                        "{0}.{1}".format(idx+1, match.end(group_name))
                    )


# lists
extensionLists = [CExtensionsList, PyExtensionsList, VHDLExtensionsList]
regexList = [Cregex, Pyregex, VHDLregex]
applyTagCalls = [applyC_Tags, applyPy_Tags, applyVHDL_Tags]
