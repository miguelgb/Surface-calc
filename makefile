FILES := main.py
BRANCH := master
COMMENTS := "Comment"

mastermainpush: 
	git add $(FILES)
	git commit -m $(COMMENTS)
	git checkout $(BRANCH)
	git fetch
	git remote -v && git push
	echo $(COMMENTS)
	git init

clean:
	rm -f ./.git/index.lock

help:
	@echo "mastermainpush: Push the current version of main.py"
	@echo "		FILES=main.py BRANCH=master COMMENTS=Comment"
	@echo ""
	@echo "clean:		Remove crashed git processes"
	@echo "		rm -f ./.git/index.lock"

