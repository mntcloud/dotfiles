;;; Commentary: in this config i use packages doom-themes magit evil flycheck go-mode use-package doom-modeline company 
;;; Melpa repo 
(require 'package)
  (add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

;; Configuration
(use-package emacs
             :init
             (add-to-list 'default-frame-alist '(ns-transparent-titlebar . t))
             (add-to-list 'default-frame-alist '(tool-bar-lines . 0))
             (add-to-list 'default-frame-alist '(vertical-scroll-bars . nil))
             (add-to-list 'default-frame-alist '(title . "Lion Emacs"))
	     (custom-set-faces '(default ((t (:height 120 :family "Menlo"))))))

(use-package doom-themes
	     :config
	     (load-theme 'doom-wilmersdorf t))
(use-package flycheck
	     :ensure t
	     :init (global-flycheck-mode))
(use-package evil
	     :ensure t
	     :init (evil-mode 1))
(use-package doom-modeline
             :ensure t
             :config
	     (doom-modeline-mode 1)
	     (setq doom-modeline-height 1)
	     (setq doom-modeline-bar-width 10)
	     (setq doom-modeline-unicode-fallback nil)
	     (setq doom-modeline-buffer-state-icon nil)
	     (setq doom-modeline-major-mode-icon nil)
	     (setq doom-modeline-major-mode-color-icon nil)
	     (setq doom-modeline-modal-icon nil)
	     (doom-modeline-def-modeline 'my-simple-line
                            '(bar matches buffer-info remote-host buffer-position parrot selection-info)
                            '(misc-info minor-modes input-method buffer-encoding major-mode process vcs ))
	     (doom-modeline-set-modeline 'my-simple-line 'default))
