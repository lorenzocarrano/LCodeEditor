import re
import tkinter as tk
import editortheme as et
#C Language --> index 0
if et.SelectedTheme == et.DefaultTheme:
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
            return_tag = f"return_{idx}"
            tags = {
                int_tag: "blue",
                float_tag: "blue",
                char_tag: "blue",
                for_tag: "green",
                while_tag: "green",
                if_tag: "purple",
                include_tag: "green",
                return_tag: "blue"
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
        r"(?P<CommentedLine>#.*)" + "|" #commented line
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
            CommentedLine_tag = f"CommentedLine_{idx}"
            tags = {
                for_tag: "purple",
                if_tag: "purple",
                import_tag: "purple",
                return_tag: "purple",
                def_tag: "purple",
                True_tag: "red",
                False_tag: "red",
                CommentedLine_tag: "gray"
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

else:
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
            return_tag = f"return_{idx}"
            tags = {
                int_tag: "#6B6BBC",
                float_tag: "#6B6BBC",
                char_tag: "#6B6BBC",
                for_tag: "orange",
                while_tag: "orange",
                if_tag: "orange",
                include_tag: "green",
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
            r"(?P<CommentedLine>#.*)" + "|" #commented line
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
            CommentedLine_tag = f"CommentedLine_{idx}"
            tags = {
                for_tag: "orange",
                if_tag: "orange",
                import_tag: "orange",
                return_tag: "orange",
                def_tag: "orange",
                True_tag: "red",
                False_tag: "red",
                CommentedLine_tag: "gray"
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
#lists
regexList = [Cregex, Pyregex]
applyTagCalls = [applyC_Tags, applyPy_Tags]
