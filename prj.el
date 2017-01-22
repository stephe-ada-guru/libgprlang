;; Emacs settings for libadalang project

(require 'sal-langkit)

(let ((default-directory (file-name-directory (or load-file-name buffer-file-name))))
  (sal-langkit-project "libgprlang" "gpr"))

;; FIXME: use project-multi-lang

;; WORKAROUND: gpr-query doesn't process library files, for some
;; reason, so we provide two ada-mode projects; one for mains, one for
;; library.
(progn
  (ada-parse-prj-file "mains.prj")
  (ada-select-prj-file "mains.prj"))

(progn
  (ada-parse-prj-file "lib.prj")
  (ada-select-prj-file "lib.prj"))


;; end of file
